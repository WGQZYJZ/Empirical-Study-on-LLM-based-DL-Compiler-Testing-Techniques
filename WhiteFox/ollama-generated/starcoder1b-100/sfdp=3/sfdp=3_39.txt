
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x, y, z):
        k_t  = self.conv(x).transpose(-2, -1)
        query = z.matmul(k_t)
        v_t  = y.matmul(z)
        scale_factor = torch.nn.functional.softmax(x)
        scaled_query = query.mul(scale_factor)
        dropout_query = torch.nn.functional.dropout(scaled_query, p=dropout_p)
        result = dropout_query.matmul(v_t).transpose(-2, -1)
        return result


# Initializing the model
m  = Model()

# Inputs to the model
x  = torch.randn(10, 3, 64, 64)
y  = torch.randn(5, 8, 128, 128)
z  = torch.randn(10, 8, 32, 32)
