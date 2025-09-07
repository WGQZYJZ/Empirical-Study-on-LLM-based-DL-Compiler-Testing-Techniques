
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, qk, x_input):
        output = torch.matmul(qk, x_input.transpose(-2, -1)) / (scale * inv_temperature)
        softmax_output = F.softmax(output / temperature, dim=-1)
        dropout_output = F.dropout(softmax_output, p=dropout_p, training=self.training)
        attention_output = torch.matmul(dropout_output, x_input) * (scale / inv_temperature)
        return attention_output


# Initializing the model
m = Model()


