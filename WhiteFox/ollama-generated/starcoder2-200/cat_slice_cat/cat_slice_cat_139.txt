
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.cat = torch.nn.Flatten()
        self.sl = torch.nn.Flatten()
 
    def forward(self, x0):
        v1  = [x0] * size
        v2  = self.cat(*v1) # Concatenate input tensors along dimension 1 and then squeeze the concatenated tensor using a flatten operation on all its dimensions
        v3  = torch.nn.functional.split(v2, len(v1), dim=1)[0] # Slice the concatenated tensor along dimension 1 with the specified length (size)
        v4  = self.sl(*v1[::-1], v2[::].contiguous() * size) # Concatenate the original tensors and then squeeze them using a flatten operation on all its dimensions after they are reversed
        return v3, v4


# Initializing the model
m  = Model()


# Inputs to the model: 1. A list of 10 tensors; each tensor contains 2 6-by-6 tensors. 
__input_list__= [torch.nn.functional.split(x0, dim=0)[i] for i in range(len(torch.nn.functional.split(x0)))]

 # Inputs to the model: 1. A list of 2 tensors; each tensor contains 4 6-by-6 tensors. 
__input_list__ = [torch.nn.functional.split(x0, dim=0)[i] for i in range(len(torch.nn.functional.split(x0)))]

 # Inputs to the model: 1. A list of 4 tensors; each tensor contains 8 6-by-6 tensors. 
__input_list__ = [torch.nn.functional.split(x0, dim=0)[i] for i in range(len(torch.nn.functional.split(x0)))]

 # Inputs to the model: 1. A list of 8 tensors; each tensor contains 4 6-by-6 tensors.
__input_list__ = [torch.nn.functional.split(x0, dim=0)[i] for i in range(len(torch.nn.functional.split(x0)))]

 # Inputs to the model: 1. A list of 8 tensors; each tensor contains 2 6-by-6 tensors.
__input_list__ = [torch.nn.functional.split(x0, dim=0)[i] for i in range(len(torch.nn.functional.split(x0)))]

 # Inputs to the model: 1. A list of 8 tensors; each tensor contains 32 6-by-6 tensors.
__input_list__ = [torch.nn.functional.split(x0, dim=0)[i] for i in range(len(torch.nn.functional.split(x0)))]

 # Inputs to the model: 1. A list of 8 tensors; each tensor contains 32 6-by-6 tensors.
__input_list__ = [torch.nn.functional.split(x0, dim=0)[i] for i in range(len(torch.nn.functional.split(x0)))]

 # Inputs to the model: 1. A list of 8 tensors; each tensor contains 32 6-by-6 tensors.
__input_list__ = [torch.nn.functional.split(x0, dim=0)[i] for i in range(len(torch.nn.functional.split(x0)))]

 # Inputs to the model: 1. A list of 8 tensors; each tensor contains 32 6-by-6 tensors.
__input_list__ = [torch.nn.functional.split(x0, dim=0)[i] for i in range(len(torch.nn.functional.split(x0)))]

 # Inputs to the model: 1. A list of 8 tensors; each tensor contains 32 6-by-6 tensors.
__input_list__ = [torch.nn.functional.split(x0, dim=0)[i] for i in range(len(torch.nn.functional.split(x0)))]

 # Inputs to the model: 1. A list of 8 tensors; each tensor contains 32 6-by-6 tensors.
__input_list__ = [torch.nn.functional.split(x0, dim=0)[i] for i in range(len(torch.nn.functional.split(x0)))]

 # Inputs to the model: 1. A list of 8 tensors; each tensor contains 32 6-by-6 tensors.
__input_list__ = [torch.nn.functional.split(x0, dim=0)[i] for i in range(len(torch.nn.functional.split(x0)))]

 # Inputs to the model: 1. A list of 8 tensors; each tensor contains 32 6-by-6 tensors.
__input_list__ = [torch.nn.functional.split(x0, dim=0)[i] for i in range(len(torch.nn.functional.split(x0)))]

 # Inputs to the model: 1. A list of 8 tensors; each tensor contains 32 6-by-6 tensors.
__input_list__ = [torch.nn.functional.split(x0, dim=0)[i] for i in range(len(torch.nn.functional.split(x0)))]

 # Inputs to the model: 1. A list of 8 tensors; each tensor contains 32 6-by-6 tensors.
__input_list__ = [torch.nn.functional.split(x0, dim=0)[i] for i in range(len(torch.nn.functional.split(x0)))]

 # Inputs to the model: 1. A list of 8 tensors; each tensor contains 32 6-by-6 tensors.
__input_list__ = [torch.nn.functional.split(x0, dim=0)[i] for i in range(len(torch.nn.functional.split(x0)))]

 # Inputs to the model: 1. A list of 8 tensors; each tensor contains 32 6-by-6 tensors.
__input_list__ = [torch.nn.functional.split(x0, dim=0)[i] for i in range(len(torch.nn.functional.split(x0)))]

 # Inputs to the model: 1. A list of 8 tensors; each tensor contains 32 6-by-6 tensors.
__input_list__ = [torch.nn.functional.split(x0, dim=0)[i] for i in range(len(torch.nn.functional.split(x0)))]

 # Inputs to the model: 1. A list of 8 tensors; each tensor contains 32 6-by-6 tensors.
__input_list__ = [torch.nn.functional.split(x0, dim=0)[i] for i in range(len(torch.nn.functional.split(x0)))]

 # Inputs to the model: 1. A list of 8 tensors; each tensor contains 32 6-by-6 tensors.
__input_list__ = [torch.nn.functional.split(x0, dim=0)[i] for i in range(len(torch.nn.functional.split(x0)))]

 # Inputs to the model: 1. A list of 8 tensors; each tensor contains 32 6-by-6 tensors.
__input_list__ = [torch.nn.functional.split(x0, dim=0)[i] for i in range(len(torch.nn.functional.split(x0)))]

 # Inputs to the model: 1. A list of 8 tensors; each tensor contains 32 6-by-6 tensors.
__input_list__ = [torch.nn.functional.split(x0, dim=0)[i] for i in range(len(torch.nn.functional.split(x0)))]

 # Inputs to the model: 1. A list of 8 tensors; each tensor contains 32 6-by-6 tensors.
__input_list__ = [torch.nn.functional.split(x0, dim=0)[i] for i in range(len(torch.nn.functional.split(x0)))]

 # Inputs to the model: 1. A list of 8 tensors; each tensor contains 32 6-by-6 tensors.
__input_list__ = [torch.nn.functional.split(x0, dim=0)[i] for i in range(len(torch.nn.functional.split(x0)))]

 # Inputs to the model: 1. A list of 8 tensors; each tensor contains 32 6-by-6 tensors.
__input_list__ = [torch.nn.functional.split(x0, dim=0)[i] for i in range(len(torch.nn.functional.split(x0)))]

 # Inputs to the model: 1. A list of 8 tensors; each tensor contains 32 6-by-6 tensors.
__input_list__ = [torch.nn.functional.split(x0, dim=0)[i] for i in range(len(torch.nn.functional.split(x0)))]

 # Inputs to the model: 1. A list of 8 tensors; each tensor contains 32 6-by-6 tensors.
__input_list__ = [torch.nn.functional.split(x0, dim=0)[i] for i in range(len(torch.nn.functional.split(x0)))]

 # Inputs to the model: 1. A list of 8 tensors; each tensor contains 32 6-by-6 tensors.
__input_list__ = [torch.nn.functional.split(x0, dim=0)[i] for i in range(len(torch.nn.functional.split(x0)))]

 # Inputs to the model: 1. A list of 8 tensors; each tensor contains 32 6-by-6 tensors.
__input_list__ = [torch.nn.functional.split(x0, dim=0)[i] for i in range(len(torch.nn.functional.split(x0)))]

 # Inputs to the model: 1. A list of 8 tensors; each tensor contains 32 6-by-6 tensors.
__input_list__ = [torch.nn.functional.split(x0, dim=0)[i] for i in range(len(torch.nn.functional.split(x0)))]

 # Inputs to the model: 1. A list of 8 tensors; each tensor contains 32 6-by-6 tensors.
__input_list__ = [torch.nn.functional.split(x0, dim=0)[i] for i in range(len(torch.nn.functional.split(x0)))]

 # Inputs to the model: 1. A list of 8 tensors; each tensor contains 32 6-by-6 tensors.
__input_list__ = [torch.nn.functional.split(x0, dim=0)[i] for i in range(len(torch.nn.functional.split(x0)))]

 # Inputs to the model: 1. A list of 8 tensors; each tensor contains 32 6-by-6 tensors.
__input_list__ = [torch.nn.functional.split(x0, dim=0)[i] for i in range(len(torch.nn.functional.split(x0)))]

 # Inputs to the model: 1. A list of 8 tensors; each tensor contains 32 6-by-6 tensors.
__input_list__ = [torch.nn.functional.split(x0, dim=0)[i] for i in range(len(torch.nn.functional.split(x0)))]

 # Inputs to the model: 1. A list of 8 tensors; each tensor contains 32 6-by-6 tensors.
__input_list__ = [torch.nn.functional.split(x0, dim=0)[i] for i in range(len(torch.nn.functional.split(x0)))]

 # Inputs to the model: 1. A list of 8 tensors; each tensor contains 32 6-by-6 tensors.
__input_list__ = [torch.nn.functional.split(x0, dim=0)[i] for i in range(len(torch.nn.functional.split(x0)))]

 # Inputs to the model: 1. A list of 8 tensors; each tensor contains 32 6-by-6 tensors.
__input_list__ = [torch.nn.functional.split(x0, dim=0)[i] for i in range(len(torch.nn.functional.split(x0)))]

 # Inputs to the model: 1. A list of 8 tensors; each tensor contains 32 6-by-6 tensors.
__input_list__ = [torch.nn.functional.split(x0, dim=0)[i] for i in range(len(torch.nn.functional.split(x0)))]

 # Inputs to the model: 1. A list of 8 tensors; each tensor contains 32 6-by-6 tensors.
__input_list__ = [torch.nn.functional.split(x0, dim=0)[i] for i in range(len(torch.nn.functional.split(x0)))]

 # Inputs to the model: 1. A list of 8 tensors; each tensor contains 32 6-by-6 tensors.
__input_list__ = [torch.nn.functional.split(x0, dim=0)[i] for i in range(len(torch.nn.functional.split(x0)))]

 # Inputs to the model: 1. A list of 8 tensors; each tensor contains 32 6-by-6 tensors.
__input_list__ = [torch.nn.functional.split(x0, dim=0)[i] for i in range(len(torch.nn.functional.split(x0)))]

 # Inputs to the model: 1. A list of 8 tensors; each tensor contains 32 6-by-6 tensors.
__input_list__ = [torch.nn.functional.split(x0, dim=0)[i] for i in range(len(torch.nn.functional.split(x0)))]

 # Inputs to the model: 1. A list of 8 tensors; each tensor contains 32 6-by-6 tensors.
__input_list__ = [torch.nn.functional.split(x0, dim=0)[i] for i in range(len(torch.nn.functional.split(x0)))]

 # Inputs to the model: 1. A list of 8 tensors; each tensor contains 32 6-by-6 tensors.
__input_list__ = [torch.nn.functional.split(x0, dim=0)[i] for i in range(len(torch.nn.functional.split(x0)))]

 # Inputs to the model: 1. A list of 8 tensors; each tensor contains 32 6-by-6 tensors.
__input_list__ = [torch.nn.functional.split(x0, dim=0)[i] for i in range(len(torch.nn.functional.split(x0)))]

 # Inputs to the model: 1. A list of 8 tensors; each tensor contains 32 6-by-6 tensors.
__input_list__ = [torch.nn.functional.split(x0, dim=0)[i] for i in range(len(torch.nn.functional.split(x0)))]

 # Inputs to the model: 1. A list of 8 tensors; each tensor contains 32 6-by-6 tensors.
__input_list__ = [torch.nn.functional.split(x0, dim=0)[i] for i in range(len(torch.nn.functional.split(x0)))]

 # Inputs to the model: 1. A list of 8 tensors; each tensor contains 32 6-by-6 tensors.
__input_list__ = [torch.nn.functional.split(x0, dim=0)[i] for i in range(len(torch.nn.functional.split(x0)))]

 # Inputs to the model: 1. A list of 8 tensors; each tensor contains 32 6-by-6 tensors.
__input_list__ = [torch.nn.functional.split(x0, dim=0)[i] for i in range(len(torch.nn.functional.split(x0)))]

 # Inputs to the model: 1. A list of 8 tensors; each tensor contains 32 6-by-6 tensors.
__input_list__ = [torch.nn.functional.split(x0, dim=0)[i] for i in range(len(torch.nn.functional.split(x0)))]

 # Inputs to the model: 1. A list of 8 tensors; each tensor contains 32 6-by-6 tensors.
__input_list__ = [torch.nn.functional.split(x0, dim=0)[i] for i in range(len(torch.nn.functional.split(x0)))]

 # Inputs to the model: 1. A list of 8 tensors; each tensor contains 32 6-by-6 tensors.
__input_list__ = [torch.nn.functional.split(x0, dim=0)[i] for i