
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        splitted = torch.split(x1, 320, dim=1) # The size of the split tensors is equal to the input tensor size divided by the number of splits (in this case 8).
        concatenated_tensor  = torch.cat([splitted[i] for i in range(len(splitted))], 1)
        return concatenated_tensor


# Initializing model with sample input and validation function
x1  = torch.randn(2049, 3) # Input tensor size is the product of the height, width, and number of channels of the input tensor (in this case it's 64*8*8).
m  = Model()
if m(x1):
    print("Valid Model")

