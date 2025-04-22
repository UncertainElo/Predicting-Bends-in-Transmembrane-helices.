from Bio.PDB.MMCIF2Dict import MMCIF2Dict
import numpy as np

# Define a function to calculate distance between two points
def calculate_distance(coord1, coord2):
    return np.linalg.norm(np.array(coord1) - np.array(coord2))

# File to store results
with open('Coordinates_of_atoms.txt', 'a') as fd:
    for i in range(2704, 2872):
        pdb_info = MMCIF2Dict("287.cif")

        if '_struct_conf.pdbx_PDB_helix_length' in pdb_info:
            length = len(pdb_info['_struct_conf.pdbx_PDB_helix_length'])

            for j in range(length):
                if int(pdb_info['_struct_conf.pdbx_PDB_helix_length'][j]) >= 20:
                    # Get the sequence id in figures of beginning and end
                    a = pdb_info['_struct_conf.beg_label_seq_id'][j]
                    b = pdb_info['_struct_conf.end_label_seq_id'][j]
                    
                    # Get the chain character of the beginning of the helix
                    c = pdb_info['_struct_conf.beg_label_asym_id'][j]

                    # Finding index of the chain character in the atom info.
                    chain_indices = [k for k, chain_id in enumerate(pdb_info['_atom_site.label_asym_id']) if chain_id == c]

                    # Find the starting and ending points of the helix
                    index_beg = next(k for k in chain_indices if pdb_info['_atom_site.label_seq_id'][k] == a)
                    index_end = next(k for k in chain_indices if pdb_info['_atom_site.label_seq_id'][k] == b)

                    # Find indices of Oxygen and Nitrogen atoms within the helix range
                    index_O = [k for k in range(index_beg, index_end + 1) if pdb_info['_atom_site.label_atom_id'][k] == 'O']
                    index_N = [k for k in range(index_beg, index_end + 1) if pdb_info['_atom_site.label_atom_id'][k] == 'N']

                    for l in range(len(index_O) - 3):
                        O_coord = (float(pdb_info['_atom_site.Cartn_x'][index_O[l]]),
                                   float(pdb_info['_atom_site.Cartn_y'][index_O[l]]),
                                   float(pdb_info['_atom_site.Cartn_z'][index_O[l]]))

                        N_coord = (float(pdb_info['_atom_site.Cartn_x'][index_N[l + 4]]),
                                   float(pdb_info['_atom_site.Cartn_y'][index_N[l + 4]]),
                                   float(pdb_info['_atom_site.Cartn_z'][index_N[l + 4]]))

                        distance = calculate_distance(O_coord, N_coord)
                        if distance > 3.5:
                            p = int(index_O[l]) + 1
                            q = int(index_N[l + 4]) + 1
                            fd.write(f"{i}.cif, {p:<5}, {pdb_info['_atom_site.label_seq_id'][int(p)]:<4}, {q:<4} ,{pdb_info['_atom_site.label_seq_id'][q]:<4} ,{distance:<20}\n")
        
        print(f"{i}.cif done")
      # {c} 
