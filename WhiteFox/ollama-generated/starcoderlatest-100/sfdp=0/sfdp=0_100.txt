
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(512, 3072)
 
    def forward(self, v1, v2, k1, k2):
        attention_output = torch.matmul(v2, torch.transpose(k1, -1, -2)) / math.sqrt(k1.shape[-1])
 
        attention_output = torch.nn.Softmax()(attention_output)
        context = torch.matmul(attention_output, v1)
        return context

# Initializing the model
a = Attention()


