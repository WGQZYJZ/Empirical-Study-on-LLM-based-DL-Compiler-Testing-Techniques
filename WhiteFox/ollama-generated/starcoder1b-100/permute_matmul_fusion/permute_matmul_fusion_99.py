
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 2)
        self.linear2 = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1)
        v2 = x2.permute(0, 2, 1)
        # Add code here: Bmm and Matmul
        return __output__


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 2, 2)
__output = m(x1, x2)


# ## References
> [[arXiv]](https://arxiv.org/abs/1807.03684) | [GitHub](https://github.com/zju-ml/Model-Checking-and-Mutation-Testing-for-Machine-Learning-Based-Deep-Learning)

