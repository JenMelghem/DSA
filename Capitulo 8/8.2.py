class ExpressionTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class ExpressionTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if not self.root:
            self.root = ExpressionTreeNode(value)
        else:
            self._insert_recursively(self.root, value)
    
    def _insert_recursively(self, node, value):
        pass  # Implementar aquí la inserción recursiva de nodos
        
    def print_tree(self):
        pass  # Implementar aquí la impresión del árbol
    
    def print_tree(self):
        self._print_tree_recursive(self.root, 0)

    def _print_tree_recursive(self, node, level):
        if node is not None:
            self._print_tree_recursive(node.right, level + 1)
            print("   " * level + str(node.value))
            self._print_tree_recursive(node.left, level + 1)

         
    def levels(self):          # Count the levels in the tree
      return self.__levels(self.__root) # Count starting at root
   
    def __levels(self, node):  # Recursively count levels in subtree
      if node:                # If a node is provided, then level is 1
         return 1 + max(self.__levels(node.leftChild),  # more than
                        self.__levels(node.rightChild)) # max child
      else: return 0          # Empty subtree has no levels

    def build_expression_tree(self, expression):
        tokens = expression.split()
        operator_stack = []
        output_queue = []
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        
        for token in tokens:
            if token.isdigit():
                output_queue.append(token)
            elif token in '+-*/':
                while (operator_stack and operator_stack[-1] in '+-*/' and
                       precedence[operator_stack[-1]] >= precedence[token]):
                    output_queue.append(operator_stack.pop())
                operator_stack.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output_queue.append(operator_stack.pop())
                operator_stack.pop()
        
        while operator_stack:
            output_queue.append(operator_stack.pop())
        
        print("Postfix expression:", output_queue)  # Imprimir notación posfija
        
        # Construir el árbol de expresiones usando notación posfija
        expression_stack = []
        for token in output_queue:
            if token.isdigit():
                expression_stack.append(ExpressionTreeNode(token))
            elif token in '+-*/':
                right_operand = expression_stack.pop()
                left_operand = expression_stack.pop()
                operator_node = ExpressionTreeNode(token)
                operator_node.left = left_operand
                operator_node.right = right_operand
                expression_stack.append(operator_node)
        
        self.root = expression_stack[0] if expression_stack else None
        
    def evaluate(self, node=None):
        if node is None:
            node = self.root
        
        if node.value.isdigit():
            return int(node.value)
        else:
            left_value = self.evaluate(node.left)
            right_value = self.evaluate(node.right)
            if node.value == '+':
                return left_value + right_value
            elif node.value == '-':
                return left_value - right_value
            elif node.value == '*':
                return left_value * right_value
            elif node.value == '()':
                return left_value * right_value
            elif node.value == '/':
                return left_value / right_value

# Crear un árbol de expresiones
expression_tree = ExpressionTree()


# Construir el árbol de expresiones a partir de una expresión matemática
expression = "3 * 4 - 5 / 2"
expression_tree.build_expression_tree(expression)

# Imprimir el árbol de expresiones (implementación opcional)
# expression_tree.print_tree()

# Evaluar la expresión utilizando el árbol de expresiones
result = expression_tree.evaluate()
print("Resultado de la expresión:", result)
print("----")
expression_tree.print_tree()
print("------")

