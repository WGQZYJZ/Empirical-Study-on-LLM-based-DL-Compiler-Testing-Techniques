
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, y1):  # x2 and y2 are not used as arguments.
        v1 = torch.randn(3)
        v2 = input_tensor_A.permute([1]).view(-1)  # Permute the input tensor A
        t1 = input_tensor_B.permute([0, 2, 1]) 
        v4 = torch.bmm(t1, v2.view(v2.size() + (3, )))
        return v1, v2, v4

# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(2) 
 __output__   = m(input_tensor_A, input_tensor_B)
