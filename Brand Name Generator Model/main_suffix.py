from tensorflow.keras.callbacks import LambdaCallback
import numpy as np
from keras.models import load_model

chars = ['\n', "'", 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ','_','-','.','/','&','1','2','3','4','5','6','7','8','9','0','+','(',')','>','<','%','`']

char_indices = dict((c, i) for i, c in enumerate(chars))
indices_char = dict((i, c) for i, c in enumerate(chars))

maxlen = 33
minlen = 1

model = load_model('model_suffix.h5')

def sample(preds):
    """ function that sample an index from a probability array """
    preds = np.asarray(preds).astype('float64')
    preds = preds / np.sum(preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.random.choice(range(len(chars)), p = probas.ravel())

def print_name_generated(name):
    print(name[::-1], flush=True)
    
def print_list_generated(lst):
    print([l[::-1] for l in lst], flush=True)
    
    
def generate_new_names(*args):
    print("----------Generating names----------")

    # Add pre-padding of zeros in the input.
    sequence = ('{0:0>' + str(maxlen) + '}').format(prefix).lower()

    # tmp variables
    tmp_generated = prefix
    list_outputs = list()

    while (len(list_outputs) < max_names):

        # Vectorize the input of the model.
        x_pred = np.zeros((1, maxlen, len(chars)))
        for t, char in enumerate(sequence):
            if char != '0':
                x_pred[0, t, char_indices[char]] = 1

        # Predict the probabilities of the next char.
        preds = model.predict(x_pred, verbose=0)[0]

        # Chose one based on the distribution obtained in the output of the model.
        next_index = sample(preds)
        # Get the corresponding char.
        next_char = indices_char[next_index]

        # If the char is a new line character or the name start to be bigger than the longest word, 
        # try to add it to the list and reset temp variables.
        if next_char == '\n' or len(tmp_generated) > maxlen:
            
            # If the name generated is not in the list, append it and print it.
            if tmp_generated not in list_outputs:
                list_outputs.append(tmp_generated)
                print_name_generated(tmp_generated)
            # Reset tmp variables
            sequence = ('{0:0>' + str(maxlen) + '}').format(prefix).lower()
            tmp_generated = prefix
        else:
    
            # Append the char to the sequence that we're generating.
            tmp_generated += next_char
            # Add pre-padding of zeros to the sequence generated and continue.
            sequence = ('{0:0>' + str(maxlen) + '}').format(tmp_generated).lower()

    print("-----------------End-----------------")
    
# Function invoked at the end of each epoch. Prints generated names.
callback = LambdaCallback(on_epoch_end=generate_new_names)    

    
    
    
    
if __name__ == '__main__':
    suffix = "don"
    # Insert how many names you'd like to generate:
    max_names = 10

    # This reverse the prefix 
    prefix = suffix[::-1]
    generate_new_names()