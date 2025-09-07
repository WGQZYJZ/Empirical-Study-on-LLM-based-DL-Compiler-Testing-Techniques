
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.q = torch.nn.Linear(768, 3072) # query (hidden_size x model_dim)
        self.k = torch.nn.Linear(768, 3072) # key (hidden_size x model_dim)
        self.v = torch.nn.Linear(768, 3072) # value (hidden_size x model_dim)
 
    def forward(self, query, key, value):
        qk = self.q(query).view(-1, 768, 3072) # (bs * slen, head_num, head_size)
        kg = self.k(key).view(-1, 768, 3072) # (bs * slen, head_num, head_size)
        vv = self.v(value).view(-1, 768, 3072) # (bs * slen, head_num, head_size)
 
        qk = qk.transpose(0, 1).contiguous().view(-1, 3072, 768) # (slen * bs, head_num, hidden_size)
        kg = kg.transpose(0, 1).contiguous().view(-1, 3072, 768) # (slen * bs, head_num, hidden_size)
        vv = vv.transpose(0, 1).contiguous().view(-1, 3072, 768) # (slen * bs, head_num, hidden_size)
 
        softmax_qk = torch.nn.functional.softmax(qk / math.sqrt(self.head_size), dim=-1) # (slen * bs, head_num, hidden_size)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # (slen * bs, head_num, hidden_size)
 
        output = dropout_qk.matmul(vv) # (slen * bs, head_num, head_size)
        output = output.transpose(0, 1).contiguous().view(-1, self.hidden_size, 768) # (bs, slen * head_num, hidden_size)
 
        return output


# Initializing the model
a = Attention()


# Inputs to the model
query = torch.randn(12, 768, 3072) # (batch_size, head_num, hidden_size)
key = torch.randn(12, 768, 3072) # (batch_size, head_num, hidden_size)
value = torch.randn(12, 768, 3072) # (batch_size, head_num, hidden_size)
