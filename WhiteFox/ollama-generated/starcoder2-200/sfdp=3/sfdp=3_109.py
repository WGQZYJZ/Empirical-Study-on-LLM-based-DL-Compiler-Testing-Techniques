

class Model(torch.nn.Module):
    def __init__(self,
                 hidden_size=768,
                 num_attention_heads=12,
                 dropout=0.1):
        super().__init__()
        self.hidden_size = hidden_size
        self.num_attention_heads = num_attention_heads
        self.dropout = dropout
 
        # 3 is the number of tensors in the key tensor
        key_tensor  = torch.nn.Parameter(torch.randn(2, 100))
        value_tensor = torch.nn.Parameter(torch.randn(54978360, 100))
 
        self._scale_factor  = float(self.hidden_size) / \
            float(num_attention_heads) ** float(.5)
 
        self.key = key_tensor
        self.value = value_tensor
 
    def forward(self):
        v2  = torch.nn.functional.dropout(self._softmax(self._qk), p=0.8, inplace=False)
        v3  = v2 .matmul(self.value) 
        return v3

    @staticmethod
    def _softmax(input_tensor):
        return input_tensor.softmax(-1)


# Initializing the model