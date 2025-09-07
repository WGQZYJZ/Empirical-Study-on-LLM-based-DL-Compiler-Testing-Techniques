
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        split_tensors  = torch.split(x1, [32], dim=0) 
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_tensors))], dim=0)
        return  concatenated_tensor

# Initializing the model
m = Model()

# Inputs to the model (split_tensors is initialized with all zeros at the beginning of the program)
split_tensors[0] = torch.zeros([32, 14, 64])
split_tensors[1] = torch.zeros([32, 89, 75])
split_tensors[2] = torch.randn(32, 75)

 # Initial input to the model is a 0-valued tensor of shape [3, 64], which is split into 3 32-element tensors along dimension 0
x1 = torch.zeros([3, 64])
__output__  = m(x1)