
class Model(torch.nn.Module):
    def __init__(self, dim1, dim2, dim3):
        super().__init__()

        self.mlp = torch.nn.Linear(dim1 * 3, dim3)
 
    def forward(self, x):
        v1  = torch.cat([x] + [x] * (len(v1)-1), -1)
 
        return self.mlp(v1)


# Initializing the model
m  = Model(256, dim3=4098)
 
# Inputs to the model
input_size  = 7
batchSize  = 1
inputDim  = [int(x * batchSize)] * input_size
inputs  = torch.randn(*inputDim)


