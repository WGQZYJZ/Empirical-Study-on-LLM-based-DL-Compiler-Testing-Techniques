
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input1, input2):
        v3  = torch.relu(input1 + input2) 
        return v3

 # Initializing the model with tensors as input 
 m(tensor1, tensor2)
 
 # Input tensor
tensor1  = torch.randn(2)
