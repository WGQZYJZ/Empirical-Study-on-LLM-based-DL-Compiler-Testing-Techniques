
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        # A convolution is implemented with a two-stage implementation (the first stage is applied on the input_tensor and passed as an argument to `convNd`) and the second stage is a one-layer activation function. 
        conv = torch.nn.functional.conv2d(x1, x2)
        bn  = torch.nn.functional.batch_norm2d(input_tensor=conv)
        return bn

# Initializing the model
m  = Model()


