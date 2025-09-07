
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.cat([x1 for i in range(2)], dim=0)
        v3  = torch.randn(v1.shape[0], 84, 96) 
        v5  = torch.cat((v1, v3), dim=1)
        return v5

# Initializing the model
m  = Model()

# Input to the model
input_tensor = [torch.randn(2, 84, 96)]

# Generating input tensors for torch.cat, torch.nn.functional.softmax with size 10 x 84 x 96; torch.nn.functional.softmax with size 5 x 73129; torch.nn.functional.relu with size 387 x 84
input_tensor = [torch.randn(x, 84, 96) for x in (10, 5, 3)]
__output__  = m(*input_tensor)

