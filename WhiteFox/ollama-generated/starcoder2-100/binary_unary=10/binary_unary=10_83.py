
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):

        v2  = torch.zeros((x1.shape[0], x1.shape[-3], x1.shape[-2]))
        v4 = self._make_new()
        v5  = 0 * (v2 + v4) # In the first step, multiplying each element in the result by zero to obtain an output of shape [N, 16, 8]. This is followed by a call to the function _make_new(). 
        v3 = torch.zeros(x5.shape[0], x5.shape[-3], x5.shape[-2])
        v4 = self._make_new()

        return v4

# Initializing the model
m  = Model()

# Inputs to the model
input1  = np.random.uniform(size=(1, 80)) # A 3D array with shape [N, 576]
__output__  = m(_make_new(input1))
