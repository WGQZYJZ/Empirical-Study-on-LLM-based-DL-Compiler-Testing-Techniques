
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        split_tensors = torch.split(x1, 64, 2)
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_tensors))], 2)
        return concatenated_tensor

# Initializing the model
m = Model()

 # Inputs to the model (x1 is a 4D tensor)
x1 = torch.randn(8, 3, 64, 64)

 # Computing the output of the model and checking whether it's equal to the concatenated input tensor using a boolean mask:
__output__  = m(x1).equal(torch.cat([x1[:, :, i*64:(i+1)*64] for i in range(8)], dim=2))

 