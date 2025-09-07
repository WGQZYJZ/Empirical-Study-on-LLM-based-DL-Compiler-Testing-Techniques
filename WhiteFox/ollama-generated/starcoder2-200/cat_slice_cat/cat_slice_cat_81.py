
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input0, input1):
        t1 = torch.cat([input0, input1], dim=1)
        t2 = t1[:, 0:9223372036854775807]
        t3 = t2[:, 0:size] 
        t4 = torch.cat([t1, t3], dim=1)
        return t4


# Initializing the model with some input tensor size
m  = Model(input0=torch.randn(3,8), input1=torch.randn(27,5)) # Size of input tensors may vary between executions. This value is used to generate the slicing parameter.
