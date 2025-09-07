
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.Linear(128, 512)
        self.v  = torch.nn.Sequential(
            torch.nn.Linear(512, 1),
            torch.nn.Softmax(dim=1))
 
    def forward(self, x1):
        qk = self.attn(x1)  # Apply linear transformation of the query and key tensors
        attn_weight = self.v(qk)  # Compute the weighted sum from the dot product result
        output = attn_weight @ x1  # Compute the output of the dot product
        return output


# Initializing the model
m = Model()
x1 = torch.randn(1, 3, 64, 64)
