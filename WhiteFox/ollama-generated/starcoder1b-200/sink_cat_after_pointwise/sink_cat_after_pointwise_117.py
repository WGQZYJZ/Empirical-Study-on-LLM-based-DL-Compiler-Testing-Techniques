
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @staticmethod
    def sink_cat_after_pointwise():
        return 'Some operation'

    def forward(x1, x2, ...):  # All arguments are optional
        if self.sink_cat_after_pointwise() == 'None':
            res = torch.cat([torch.ones_like(t1), torch.zeros_like(t2)], dim=0)
        else:
            res = t3.view(-1, 1).permute(0, 2, 1)

        ...  # Here, you can use a new tensor as an input to the computation

        return res


# Initializing the model
m = Model()


