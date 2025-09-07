
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 * 0.5
        v3  = v2 ** 3
        v4  = v3 * 0.044715
        v5  = v1 + v4
        v6  = v5 * 0.7978845608028654
        v7  = torch.tanh(v6)
        v8  = v7 + 1
        v9  = v2 * v8
        return v9

# Initializing the model
m_diff = Model()

# Inputs to the new model, different from the previous one
x1_diff = torch.randn(1, 3, 64, 64) + (torch.rand(1, 3, 64, 64)-0.5)
__output__m_diff = m_diff(x1_diff)

# Initializing the model with the same initial weights and biases as the model we used in the previous section; that is why we can use `torch.save()` and `torch.load()`. 
m  = Model()
torch.save(m, 'model.pt')

