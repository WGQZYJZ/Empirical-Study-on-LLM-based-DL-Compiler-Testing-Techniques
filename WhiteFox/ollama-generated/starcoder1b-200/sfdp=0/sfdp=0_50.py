
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(512, 384)
        self.key    = torch.nn.Linear(64, 384)
        self.value  = torch.nn.Linear(512, 256)
 
    def forward(self, x):
        b_size, c_in, height, width = x.shape

        h1, w1 = int(height / 4), int(width / 4)
        self.query = F.interpolate(self.query, scale_factor=2, mode="bilinear", align_corners=True)
        self.key    = F.interpolate(self.key,   scale_factor=16, mode="bilinear", align_corners=True)
        self.value  = F.interpolate(self.value, scale_factor=8, mode="bilinear", align_corners=True)

        query_layer  = x[:, :h1 * w1]
        key_layer    = x[:, h1:h1+h1*w1]
        value_layer  = x[:, h1+1:h1+h1*w1+1]

        # Compute Scaled Dot-Product Attention
        attention = torch.bmm(query_layer, key_layer.transpose(-2, -1)) / math.sqrt(float(c_in))
        attention = F.softmax(attention, dim=-1)
        output    = torch.bmm(attention, value_layer)

        # Compute Global Average Pooling
        return output.mean(dim=1, keepdim=True)


# Initializing the model
m = Model()


# Inputs to the model
x  = torch.randn(32, 512, 10, 10)
