
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input):
        output = torch.split(input, 1024, dim=3) # Split the input tensor along dimension 3 into 5 tensors of size 1024 each
        output = torch.cat([tensor for tensor in output], dim=3) # Concatenate these split tensors back to a single tensor using the same dimension (dimension 3)
        return output


# Initializing the model
m = Model()
 
# Inputs to the model
input1 = torch.randn(2, 4096, 578, 512) # Generate a random input of size [2 x 4096 x 578 x 512]
