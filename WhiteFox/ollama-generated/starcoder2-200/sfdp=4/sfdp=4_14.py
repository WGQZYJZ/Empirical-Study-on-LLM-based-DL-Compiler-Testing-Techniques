

import torch
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, d_model, num_heads=8) -> None:
        super().__init__()
        self.num_heads = num_heads
        self.d_k = d_model // num_heads
        self.d_v = d_model

        self.query_layer  = torch.nn.Linear(d_model, d_model)
        self.key_layer  = torch.nn.Linear(d_model, d_model)
        self.value_layer  = torch.nn.Linear(d_model, d_model)

        # TODO: Add one more linear layer here
        self.output_layer  = torch.nn.Linear(num_heads * self.d_v, d_model)

    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor) -> torch.Tensor:

        qk = self.__compute_att_weights__(query, key).transpose(-2, -1) / math.sqrt(query.size(-1))
        qk  += torch.full(qk.shape, float("-inf")).to(device=query.device) # Apply the mask
        attn_weight = torch.softmax(qk, dim=-1) # Softmax

        # Compute the dot product of the attention weights and the value tensor. Use self.__compute_output__() to compute this dot product
        output  = __compute_output__(attn_weight, value)

        # Normalize the output by the number of heads so that it has the same size as the output of the original linear layer (before applying the Softmax function).
        output /= math.sqrt(self.num_heads * self.d_k) # divide each element in the result by sqrt(self.d_model // self.d_v)

        return self.__output__(output)

    def __compute_att_weights__(self, query: torch.Tensor, key: torch.Tensor):
        # Compute the dot product of the query and key tensors. This is the first part of scaled dot-product attention 
        # (the matrix multiplication is not performed yet). The results are returned from the function as a tensor with size (batch_size x sequence_length_q x num_heads)

        q1 = self.__query__(query)
        k1  = self.key_layer(key)
        return torch.einsum("bijk, bikl -> bijkl", q1, k1).permute(0, 2, 3, 1)

    def __compute_output__(self, attn_weight: torch.Tensor, value: torch.Tensor): 
        # Compute the dot product of the attention weights and the value tensor
        # Note that the first argument here is a tensor with size (batch_size x sequence_length_k x sequence_length_q x num_heads)

        v1 = self.__value__(value)
        o1  = torch.einsum("bijkl, bikl -> bijkl", attn_weight, v1).permute(0, 3, 2, 1)
        return o1

    def __output__(self, output: torch.Tensor): 
        # Apply the linear layer to the output tensor

        return self.__output_layer__(output)

    def __query__(self, query):
        # Apply the linear layer on the query tensor

        return self.__query_layer__(query)

    def __key__(self, key):
         # Apply the linear layer on the key tensor

          return self.key_layer(key)


    def __value__(self, value: torch.Tensor):
        # Apply the linear layer to the value tensor

        return self.__value_layer__(value)


m  = MultiHeadAttention()
m