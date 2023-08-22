class BinaryTree:
    def __init__(self, data): 
        self.data = data #almacena el valor del nodo
        self.izquierdo = None
        self.derecho = None

    def combine(self, operator, tree1, tree2):
        # Crea un nuevo árbol binario con el operador como raíz y los árboles dados como hijos.
        new_tree = BinaryTree(operator)
        new_tree.izquierdo = tree1
        new_tree.derecho = tree2
        return new_tree

    def parse_expression(self, expression):
        tokens = expression.split()
        stack = []

        for token in tokens:
            if token.isdigit():
                stack.append(BinaryTree(int(token)))
            else:
                # Es un operador
                if len(stack) < 2:
                    raise Exception("Expresión inválida: se esperan más operandos antes de un operador.")
                operand2 = stack.pop()
                operand1 = stack.pop()
                tree = self.combine(token, operand1, operand2)
                stack.append(tree)

        if len(stack) != 1:
            raise Exception("Expresión inválida: hay más de una expresión algebraica en la entrada.")
        
        return stack[0]

    def pre_order_traversal(self):
        if self.data is not None:
            print(self.data, end=" ")
            if self.izquierdo:
                self.izquierdo.pre_order_traversal()
            if self.derecho:
                self.derecho.pre_order_traversal()

    def in_order_traversal(self):
        if self.data is not None:
            if self.izquierdo:
                print("(", end="")
                self.izquierdo.in_order_traversal()
            print(self.data, end="")
            if self.derecho:
                self.derecho.in_order_traversal()
                print(")", end="")

    def post_order_traversal(self):
        if self.data is not None:
            if self.izquierdo:
                self.izquierdo.post_order_traversal()
            if self.derecho:
                self.derecho.post_order_traversal()
            print(self.data, end=" ")


def main():
    expressions = [
        "91 95 + 15 + 19 + 4 *",
        "B B * A C 4 * * -",
        "A 57 #",
        "+ / #"
    ]

    for expression in expressions:
        try:
            binary_tree = BinaryTree(None)
            result_tree = binary_tree.parse_expression(expression)

            print("Expresión original:", expression)
            print("Recorrido preorden:", end=" ")
            result_tree.pre_order_traversal()
            print()
            print("Recorrido en orden:", end=" ")
            result_tree.in_order_traversal()
            print()
            print("Recorrido postorden:", end=" ")
            result_tree.post_order_traversal()
            print("\n")

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
