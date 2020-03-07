public class ChicagoStyleCheesePizza extends Pizza {

    public ChicagoStyleCheesePizza() {
        name = "Chicago Cheese";
        dough = "Extra Thick";
        sauce = "Plum Sauce";

        toppings.add("Shredded Cheese");

    }

    @Override
    void cut() {
        System.out.println("Cutting the pizza into square slices");
    }
}
