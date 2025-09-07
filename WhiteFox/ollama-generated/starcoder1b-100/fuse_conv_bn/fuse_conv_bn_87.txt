
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    # Note: the constructor is defined here because the functional API is not supported yet.
    def conv_bn(self, x1, x2=None):
        conv = torch.nn.functional.convXd(...)
        bn   = torch.nn.functional.batch_norm(conv(x1), ...)
        return bn

    # Note: the constructor is defined here because the functional API is not supported yet.
    def linear(self, x1):
        v1 = x1
        weight = ...
        bias  = ...

        return torch.nn.functional.linear(v1, weight, bias)


# Initializing the model
m = Model()


