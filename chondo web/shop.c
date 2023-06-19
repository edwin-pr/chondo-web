#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Structure to represent an item
typedef struct {
    char name[20];
    float price;
} Item;

// Function prototypes
void show_menu();
void add_item(Item cart[], Item items[], int *cart_size, int items_size);
void remove_item(Item cart[], int *cart_size);
void view_cart(Item cart[], int cart_size);

int main() {
    Item items[] = {
        {"apple", 1.00},
        {"banana", 0.50},
        {"orange", 0.75},
        {"mango", 1.50},
        {"grapes", 2.00}
    };
    int items_size = sizeof(items) / sizeof(items[0]);

    Item cart[10];
    int cart_size = 0;

    int choice;
    while (1) {
        show_menu();
        printf("Enter your choice (1-4): ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                add_item(cart, items, &cart_size, items_size);
                break;
            case 2:
                remove_item(cart, &cart_size);
                break;
            case 3:
                view_cart(cart, cart_size);
                break;
            case 4:
                printf("Thank you for using the shopping cart. Goodbye!\n");
                exit(0);
            default:
                printf("Invalid choice. Please try again.\n");
        }
    }

    return 0;
}

void show_menu() {
    printf("==== Shopping Cart ====\n");
    printf("1. Add item to cart\n");
    printf("2. Remove item from cart\n");
    printf("3. View cart\n");
    printf("4. Exit\n");
}

void add_item(Item cart[], Item items[], int *cart_size, int items_size) {
    char item_name[20];
    printf("Enter the item you want to add: ");
    scanf("%s", item_name);

    int i;
    for (i = 0; i < items_size; i++) {
        if (strcmp(item_name, items[i].name) == 0) {
            strcpy(cart[*cart_size].name, items[i].name);
            cart[*cart_size].price = items[i].price;
            (*cart_size)++;
            printf("%s added to cart.\n", item_name);
            return;
        }
    }

    printf("Item not found.\n");
}

void remove_item(Item cart[], int *cart_size) {
    char item_name[20];
    printf("Enter the item you want to remove: ");
    scanf("%s", item_name);

    int i;
    for (i = 0; i < *cart_size; i++) {
        if (strcmp(item_name, cart[i].name) == 0) {
            int j;
            for (j = i; j < (*cart_size) - 1; j++) {
                strcpy(cart[j].name, cart[j + 1].name);
                cart[j].price = cart[j + 1].price;
            }
            (*cart_size)--;
            printf("%s removed from cart.\n", item_name);
            return;
        }
    }

    printf("Item not found in cart.\n");
}

void view_cart(Item cart[], int cart_size) {
    if (cart_size == 0) {
        printf("Cart is empty.\n");
    } else {
        printf("Items in your cart:\n");
        int i;
        for (i = 0; i < cart_size; i++) {
            printf("%s: $%.2f\n", cart[i].name, cart[i].price);
        }
        float total = 0.0;
        for (i = 0; i < cart_size; i++) {
            total += cart[i].price;
        }
        printf("Total: $%.2f\n", total);
    }
}
