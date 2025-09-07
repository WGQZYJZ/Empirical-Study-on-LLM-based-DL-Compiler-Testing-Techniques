
class Model(torch.nn.Module):
    def __init__(self, sink_cat_after_pointwise=True):
        super().__init__()

        # Add more layers here
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        if sink_cat_after_pointwise:
            x3 = torch.cat([x1, x2], dim=-1)  # Concatenate inputs
            t1 = x3.permute(0, 2, 1)  # Permute concatenated input tensor
            v1 = self.linear(t1)  # Linear transformation to the permuted input tensor
        else:
            t1 = torch.cat([x1, x2], dim=0)  # Concatenate inputs
            t1 = t1.permute(0, 2, 1)  # Permute concatenated input tensor
            v1 = self.linear(t1)  # Linear transformation to the permuted input tensor

        return v1


# Initializing the model
m = Model()
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 2, 2)
