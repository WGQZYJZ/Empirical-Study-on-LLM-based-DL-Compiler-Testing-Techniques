
class Model(torch.nn.Module):
    def __init__(self, k1=4096, k2=-32768):
        super().__init__()
        self.conv  = torch.nn.Conv2d(5, 8, 3)
        self.linear_1  = torch.nn.Linear(k1, 16)
        self.linear_2  = torch.nn.Linear(-10 + k2, -4954 + k2 * (-7))
 
    def forward(self, x):
        v1 = self.conv(x)
        v2 = v1 + other # the 1st keyword argument
        return None


# Initializing the model with random inputs (without specifying the shapes of the tensors to initialize them with). Please also provide inputs to all the operations in the model.
m = Model()

inputs_shape  = [torch.Size([64, 8, 10]) for i in range(5)] # The shapes that need to be passed as arguments for initialization purposes of the tensors
inputs  = [Variable(i) for i in inputs_shape] 
