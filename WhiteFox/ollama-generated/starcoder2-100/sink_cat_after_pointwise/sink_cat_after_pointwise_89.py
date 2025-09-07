
class Model(torch.nn.Module):
    def __init__(self, n1=2048, n2=512):
        super().__init__()

        self.flatten = torch.nn.Flatten()  # This will be a sink point
        self.linear1 = torch.nn.Linear(3 * 3 * n1 + n2, n1)
        self.dropout1 = torch.nn.Dropout(0.5)
        self.linear2 = torch.nn.Linear(n1, n2)

    def forward(self, x):

        batchsize  = x.shape[0]  # The size of the first dimension is constant; however, it is important for correctness

        # Reorder inputs to be able to concatenate in the next step
        # This reordering will only be used in the sink_cat_after_pointwise optimization
        new_shape1 = [batchsize * x.shape[2], 3] + list(x.shape[1: -1])
        new_shape2 = [batchsize * (new_shape1[-2]), batchsize, new_shape1[-1]]

        inputs  = torch.cat([
            x.permute(0, 2, 1).reshape(*new_shape1),
            self.flatten(torch.randn(
                tuple([batchsize] + list(self.linear1.weight.shape[0: -1]))), inplace=True).reshape(
                    *new_shape2)], dim=-2)

        inputs = torch.relu(self.linear1(inputs))
        return self.dropout1(torch.tanh(self.linear2(inputs)))


# Initializing the model
m  = Model()

# Inputs to the model
__input1__, __input2__, __input3__ = torch.randn(1, 80, 45), torch.randn(
    6, 3 * 4096 + 512), torch.randn(1)
x1_s  = torch.empty([m.__input1__.shape[0]] + list(__input1__.shape[1:]), device=__input1__.device)
x2_s  = torch.empty([m.__input2__.shape[0]] + list(__input2__.shape[1:]), device=__input2__.device)
x3_s  = torch.empty([m.__input3__.shape[0]], device=__input3__.device)

m(x1_s, x2_s, x3_s)

