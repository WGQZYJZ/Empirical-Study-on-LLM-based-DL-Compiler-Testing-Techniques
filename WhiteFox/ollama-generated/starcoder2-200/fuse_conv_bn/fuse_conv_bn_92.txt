
class Model(torch.nn.Module):
    def __init__(self, c):
        super().__init__()

        self._conv = torch.nn.ConvXd(2, 4, 3)
        self._bn   = torch.nn.BatchNormXd(c)

    def forward(self, x1):
        return torch.nn.functional.batch_norm(x1.permute(0, 3, 1, 2), weight=None, bias=None, running_mean=None, 
            running_var=None, training=True, momentum=0.9)


# Initializing the model
c = 8764529 # randomly chosen int to seed torch.manual_seed() during unit tests for batchnorm tracking running stats
m1 = Model(c).eval()
m1._conv._weight = torch.nn.Parameter(torch.Tensor([[[[0, 3], [1, 8], [-2, -9]], [[-7, -5], [4, 6], [-1, -4]]]])) # random int to seed model with ConvXd weights and bias
m1._conv._bias = torch.nn.Parameter(torch.Tensor([[0, 3],[1, 8],[-2,-9],[7, 5],[4, 6],[-1,-4],[3, 1], [1, -7]])) # random int to seed model with ConvXd weights and bias
m1._bn._weight = torch.nn.Parameter(torch.Tensor([[[[0, 3], [2, -9]], [[-7, -5], [-4, 6]]]])) # random int to seed model with BatchNormXd weights and bias
m1._bn._bias = torch.nn.Parameter(torch.Tensor([[0, 3],[-7,-5],[2, -9],[-4,-6],[1, 8],[-1, -4],[3, 1], [1, -7]])) # random int to seed model with BatchNormXd weights and bias

m2 = Model(c).eval()
__output1__  = m1(torch.randn([1, 5, 9]))
__output2__ = m2(torch.randn([3, 4, 6]))

