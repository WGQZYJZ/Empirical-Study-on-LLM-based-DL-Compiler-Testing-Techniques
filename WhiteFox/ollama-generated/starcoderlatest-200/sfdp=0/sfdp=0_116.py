
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scaled_dot_product = torch.nn.Linear(3*7, 8)
 
    def forward(self, x1, x2, inv_scale=None):
        v1 = torch.matmul(x1, x2.transpose(-2,-1)) / inv_scale if inv_scale is not None else None
        attention_weights = self.scaled_dot_product(v1).softmax(dim=-1)
        output = torch.matmul(attention_weights, x2)
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(32, 3, 7, 7)
x2 = torch.randn(32, 8, 7, 7)
inv_scale = x1.shape[0]**-0.5
