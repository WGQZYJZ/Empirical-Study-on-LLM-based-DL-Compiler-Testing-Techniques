
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input_tensors):
        v = torch.cat(input_tensors, dim=1)[:, 0:9223372036854775807][:size] 
        return v
 
# Initializing the model
m  = Model()

 # Inputs to the model
input_tensors  = [torch.randn(1, size, 1), torch.randn(1, size)]
size = int(round((input_tensors[0].shape[-1]+ input_tensors[1].shape[-1]-3)/2)) 
 __output__  = m(input_tensors)
 
# Testcase for your implementation
__inputs__  = [torch.randn(1, size-1785693+4, 1), torch.randn(1, int(size/4)-2 + 30000, 1)]

