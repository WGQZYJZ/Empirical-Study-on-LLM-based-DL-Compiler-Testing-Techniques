
class ConvBNModel(torch.nn.Module):
    def __init__(self, conv: int = 10, bn: int = 2) -> None:
        super().__init__()
        self.conv = torch.nn.ConvXd(10, 36 + conv, kernel_size=(5, 7))
        self.bn = torch.nn.BatchNormXd(bn)

    def forward(self, input):
        conv = self.conv(input) # type: ignore[attr-defined]
        output = self.bn(conv)
        return output

m = ConvBNModel()


def train_func(*args, **kwargs):
    train = kwargs["train"] or False
    m.training = train
    m(**args)



@torch._jit_internal.weak_module  # type: ignore[attr-defined]
class WeightNormModel(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(in_channels=4, out_channels=8, kernel_size=(3, 3), bias=False)
        self.conv2 = nn.Conv2d(in_channels=7, out_channels=9, kernel_size=(2, 2), bias=True)

    def forward(self, input):
        v1 = F.weight_norm(self.conv1(input)) # type: ignore[attr-defined]
        v2 = self.conv2(v1)

        return v2


@torch._jit_internal.weak_module  # type: ignore[attr-defined]
def train(*args, **kwargs):
    m(**args) # type: ignore[call-overload]

    kwargs["train"] = True
    m(**args) # type: ignore[call-overload]


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

        self.linear1  = torch.nn.Linear(2, 40) 
        self.linear2  = torch.nn.Linear(40, 35)

    def forward(self, x1: torch.Tensor):
        v1 = F.relu(torch.nn.functional.conv2d(x1)) # type: ignore[attr-defined]
        v2 = self.linear1(v1)
        v3 = self.linear2(F.softmax(v2, 0))

        return v3

m  = Model()

# Initializing the model
inputs_to_the_model = torch.randn(5, 4, 7, 8), ...
inputs_to_the_model  # type: ignore[call-overload]

