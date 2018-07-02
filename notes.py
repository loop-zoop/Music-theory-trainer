import random
all_notes=['C','C#/Db','D', 'D#/Eb','E','F','F#/Gb','G','G#/Ab','A','A#/Bb','B']

def reorder_notes(root_note):
    for note in all_notes:
        if note==root_note:
            current_root_note=root_note
    current_index=all_notes.index(current_root_note)
    new_order=all_notes[current_index:]
    new_order.extend(all_notes[:current_index])
    return(new_order)

def build_major(root_note):
    current_scale=reorder_notes(root_note)
    major_scale=[current_scale[0],current_scale[2],current_scale[4],current_scale[5],current_scale[7],current_scale[9],current_scale[11]]
    return(major_scale)
    
#print(build_major('D'))

#for note in all_notes:
#        if isinstance(note,list):
#            for subnote in note:
#                if subnote==root_note:
#                    current_root_note=root_note
#        else:
#            if note==root_note:
#                current_root_note=root_note
#    print(current_root_note)
        
#test_major=[]
#test_major.extend([all_notes[0],all_notes[2],all_notes[4],all_notes[5],all_notes[7],all_notes[9],all_notes[11]])
#print(test_major)
    

#C_maj_Scale={'C major scale': ['C','D','E','F','G','A','B']}
C_maj_Scale={'C major scale': build_major('C')}
C_sharp_maj_Scale={'C# major scale': ['C#','D#','E#','F#','G#','A#','B#','C#']}
D_maj_Scale={'D major scale': ['D','E','F#','G','A','B','C#']}
E_flat_maj_Scale={'Eb major scale': ['Eb','F','G','Ab','Bb','C','D']}
E_maj_Scale={'E major scale': ['E','F#','G','#A','B','C#','D#']}

major_scales=[C_maj_Scale, C_sharp_maj_Scale, D_maj_Scale, E_flat_maj_Scale, E_maj_Scale]

C_maj_Triad=['C','E','G']
C_dim_Triad=['C','D#','F#']
C_sharp_maj_Triad=['C#','F','G#']
C_sharp_dim_Triad=['C#','E','G']
D_maj_Triad=['D','F#','A']
D_dim_Triad=['D','F','G#']
E_flat_maj_Triad=['Eb','G','Bb']
E_flat_dim_Triad=['Eb','G','Bb']
E_maj_Triad=['E','G#','B']
E_dim_Triad=['E','G','A#']
F_maj_Triad=['F','A','C']
F_dim_Triad=['F','Ab','B']
F_sharp_maj_Triad=['F#','A#','C#']
F_sharp_dim_Triad=['F#','A','C']
G_maj_Triad=['G','B','D']
G_dim_Triad=['G','A#','C#']
G_sharp_maj_Triad=['G#','C','D#']
G_sharp_dim_Triad=['G#','B','D']
A_maj_Triad=['A','C#','E']
A_dim_Triad=['A','C','D#']
A_sharp_maj_Triad=['A#','D','F']
A_sharp_dim_Triad=['A#','C#','E']

def random_scale():
    random_scale=random.randint(0,len(major_scales)-1)
    current_scale=major_scales[0]
    for key,value in current_scale.items():
        scale_name=key
        scale_list=value
    return(scale_name,scale_list)
#random_scale() returns a dictionary
#random_scale()[0] returns scale name (string)
#random_scale()[1] returns scale list (list of notes in the scale)

def generate_triad():
    scale_list=random_scale()[1]
    current_triad=[]
    while len(current_triad)<3:
        random_note=random.randint(0,len(scale_list)-1)
        current_note=scale_list[random_note]
        if current_note not in current_triad:
            current_triad.append(current_note)
    return(current_triad)

print(random_scale())

