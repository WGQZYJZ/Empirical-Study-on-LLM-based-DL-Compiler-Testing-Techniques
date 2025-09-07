
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x2):
         v1 = torch.cat(x2, dim=1)
         v2 = v1[:, 0:9223372036854775807] # slicing
         v3 = v2[:, 0:v1_size] # slicing
         v4 = torch.cat([v1, v3], dim=1)
        return v4

# Initializing the model
m = Model()


# Inputs to the model (the input tensors for each channel need to be concatenated together.)
input0 = [torch.randn(8)]  # 8 is the size of each sliced tensor along dimension 1
input1 = torch.randn(7, 23)  # the first input tensor contains size 9223372036854775807 and another 338 60 3 tensor 
__output__  = m([input1, input0])

