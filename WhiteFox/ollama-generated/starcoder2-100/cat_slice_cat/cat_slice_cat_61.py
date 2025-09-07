

class Model(torch.nn.Module):
    def __init__(self, size=None):
        super().__init__()

    def forward(self, inputs):

        return torch.cat([inputs[0], inputs[1][:size] ], dim = 1)


m = Model()
input1 = [] # A list of tensors
input2 = [torch.randn(7, size)]  # The first tensor is a batch of 8 input images. Each image has size 5 x 34 by 93. For each image in the batch there are 10 classes to predict. The second tensor is a batch of 8 one-hot encoded class labels
output = m(input2)

