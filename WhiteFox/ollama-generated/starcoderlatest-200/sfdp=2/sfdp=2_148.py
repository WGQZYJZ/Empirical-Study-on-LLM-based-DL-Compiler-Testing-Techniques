
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_q = torch.nn.Linear(8, 8)
 
    def forward(self, x1, x2):
        v1 = self.linear_q(x1)
        softmax_qk = v1 / math.sqrt(v1.shape[-1])
        output = (softmax_qk * x2).sum(-1, keepdim=False) # Sum the results of multiplying each value by its softmax score to obtain the final output. The sum can be interpreted as the attention weights.
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 8, 64)
x2 = torch.randn(2, 8, 64)
