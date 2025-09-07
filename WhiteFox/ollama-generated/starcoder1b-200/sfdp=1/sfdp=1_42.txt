
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        # x1: batch_size x input_channels x height x width
        v1 = self.conv(x1).unsqueeze(1)  # x1 -> batch_size x 1 x height x width
        v2 = torch.matmul(v1, x2).squeeze(1)  # v1 * v2 -> batch_size x output_channels
        v3 = torch.nn.functional.dropout(v2, p=dropout_p)  # apply dropout to the dot product
        return v3


# Initializing the model
m = Model()


