# Active_Ising_Model
This is an implementation of the Active Ising Model in Python.
##
The Active Ising model is a variant of the traditional Ising model that incorporates activity, making it suitable for studying systems out of equilibrium.

The Hamiltonian of the traditional Ising model is given by:
$$ H = -J \sum_{\langle i,j \rangle} s_i s_j - h \sum_i s_i $$

The Hamiltonian of the Active Ising model is given by:

$$
H = -\sum_{\text{sites } i} \frac{1}{2 \rho_i} \sum_{j=1}^{\rho_i} \sum_{\substack{k \neq j}} S_j^i S_k^i = -\sum_{\text{sites } i} \left[ \frac{m_i^2}{2 \rho_i} - \frac{1}{2} \right]
$$


Solon, Alexandre P., and Julien Tailleur. "Flocking with discrete symmetry: The two-dimensional active Ising model." Physical Review E 92.4 (2015): 042119.
