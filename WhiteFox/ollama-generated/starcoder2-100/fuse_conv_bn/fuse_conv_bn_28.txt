
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        conv = torch.nn.Conv2d(3, 64, kernel_size=(5, 5), stride=1)

        # Fuse the Conv and BatchNorm layers into a single layer
        output  = torch.nn.functional.batch_norm(conv(x1))

        return output

m  = Model()
