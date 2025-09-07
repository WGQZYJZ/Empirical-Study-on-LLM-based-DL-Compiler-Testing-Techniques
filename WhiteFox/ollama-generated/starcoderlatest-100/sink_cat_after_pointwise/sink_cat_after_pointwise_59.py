
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, t1, t2):
        t3 = torch.relu(t1) + torch.tanh(t2)  # This optimization is triggered by `sink_cat_after_pointwise`
        return t3

# Inputs to the model
t1 = torch.randn(4, 5, 6)  # shape (B, N1, D1) or (B, N1, 1)
t2 = torch.randn(8, 7, 9)  # shape (B, N2, D2) or (B, 1, N2, D2)
