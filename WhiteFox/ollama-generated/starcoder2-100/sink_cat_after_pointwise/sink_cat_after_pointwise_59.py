

class Model(torch.nn.Module):
    def __init__(self, input_features=2048):
        super().__init__()
        self.linear = torch.nn.Linear(input_features*5, 1)

    def forward(self, input_tensor):
        input_concatenated = torch.cat((input_tensor, input_tensor), dim=-1)
        concatenated_viewed   = input_concatenated.view(-1, self.linear.weight[0].shape[-2] * 5)

        return torch.nn.functional.relu(self.linear(concatenated_viewed))


m  = Model()
inputs  = torch.randn(32, 2048).cuda()
__output__  = m(inputs)


