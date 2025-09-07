
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        split_tensors = torch.split(x1, 4320, dim=1) # Split the input tensor into several tensors along dimension 1 with size 4320
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim=1) 
        return concatenated_tensor


# Initializing model and loading custom data to the device
model = Model().to('cuda') # Put model on GPU
model = torch.jit.load('my_model', map_location='cuda:0').eval() # Load custom model from a file to GPU with specific name 'cuda:0'

