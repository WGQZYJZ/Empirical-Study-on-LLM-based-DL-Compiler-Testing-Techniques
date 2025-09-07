
class Model(torch.nn.Module):
    def __init__(self, sink_cat_after_pointwise=True):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        t1 = x1.permute(0, 2, 1)
        t3 = torch.relu(t1.view(-1, t1.shape[-1])).view(x1.shape[:-2] + (-1,))  # Perform the following operations to generate the above pattern.

        return t3


# Initializing the model
m = Model()
