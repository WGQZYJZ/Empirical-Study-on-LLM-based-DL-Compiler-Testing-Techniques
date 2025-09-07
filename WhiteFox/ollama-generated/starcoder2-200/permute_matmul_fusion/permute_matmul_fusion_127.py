
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2): # x1 is a 3D tensor with shape [batch size X length of sequence Y1, input dimension Z] and X, Y >= 0; X=3 by default. And the permuted tensor shape is [batch size X 3, length of sequence Y1]. X can be configured in the task.
        v1 = x2 # the original input data
        v2 = v1.permute(0, 2, 1) 
        # The input data to the bmm function should be transposed before passing it to the bmm function.
        output = torch.bmm(v2, v1) 
        return output

# Initializing the model
m = Model()

