
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2, attention_mask, dropout_p=0.5):
        v1 = self.conv(x1, attention_mask=attention_mask)  # Apply pointwise convolution with kernel size 1 to the input tensor
        v2 = torch.matmul(v1, x2) / math.sqrt(self.attention_dim)  # Multiply the output of the convolution by a scaled version of the query tensor
        v3 = torch.nn.functional.dropout(v2, p=dropout_p)  # Apply dropout to the dot product of the query and key tensors
        return v3


# Initializing the model
m = Model()


