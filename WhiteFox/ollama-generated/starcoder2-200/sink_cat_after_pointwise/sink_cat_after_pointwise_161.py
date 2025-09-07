
class Model(torch.nn.Module):
    def __init__(self, num_inputs, num_outputs):
        super().__init__()
        self.linear = torch.nn.Linear(num_inputs, 2)

    def forward(self, input1):
        return self.linear(input1).relu()


# Initializing the model with random number of inputs/outputs (5-30). If we use the same number for both inputs and outputs, we will not trigger the sink_cat_after_pointwise optimization.
for num in random.sample(range(2, 7), 1):
    m = Model(num)
