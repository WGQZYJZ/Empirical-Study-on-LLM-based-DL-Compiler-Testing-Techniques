
class Model(torch.nn.Module):
    def __init__(self, config={}):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1) # t1 is permuted by the above pattern
        v2 = torch.nn.functional.dropout(v1, self.linear.weight, self.linear.bias,
                                           replace_fx=False) # the function dropout will be replaced with a custom version
        return v2


# Initializing the model
m = Model()


