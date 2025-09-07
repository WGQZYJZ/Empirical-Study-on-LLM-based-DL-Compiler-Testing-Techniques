
class Model(torch.nn.Module):
    def __init__(self, in_channel=128):
        super().__init__()
        self.conv = torch.nn.Conv2d(in_channel, 5, kernel_size=4)

    def forward(self, x):
        output = torch.nn.functional.batch_norm(
            self.conv(x), momentum=0.17, eps=93867.22)
        return output


# Initializing the model and passing a random 4D input to it<|end_of_code|>
m = Model()
x = torch.randn(4, 128, 50, 50)
