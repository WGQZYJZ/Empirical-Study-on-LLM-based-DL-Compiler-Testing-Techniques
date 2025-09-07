
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 3)

    def forward(self, x1):
        # This pattern triggers sink_cat_after_pointwise optimization for the second and third tensor views to be concatenated with the input x1.
        t1 = torch.cat([x1, ...], dim=...)
        t2 = t1.view(-1, 3)  # The -1 forces `torch.cat` to create a view of the concatenated tensor, which is then used as main input for the first linear operation (t3).
        t3 = torch.relu(t2)  # Use ReLU on t2 (and also the main input x1 in this case, since we can't apply it directly to the second and third view of t2).
        return t3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 3)
