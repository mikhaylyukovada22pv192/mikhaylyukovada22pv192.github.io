import React from "react"
import capabilitiesList from "./capabilitiesList";
import './capabilities.css'
import ElementWithButton from "../element_with_button/ElementWithButton";
import ElementWithInfoData from "../../data/ElementWithInfoData";
import {getCapabilities} from "../../api/CapabilitiesApi";

export function Capabilities() {

    const [capabilities, setCapabilities] = React.useState<ElementWithInfoData[]>(capabilitiesList);

    React.useEffect(() => {
            const get_capabilities = async () => {
                const result: ElementWithInfoData[] | null = await getCapabilities();
               if (result !== undefined && result !== null) {
                    setCapabilities(result)
                }
            }
            get_capabilities()
        },
        []
    );

    const elementComponents: JSX.Element[] = capabilities.map(op =>
        <ElementWithButton
            key={op.id}
            id={op.id}
            img_name={op.img_name}
            title={op.title}
            description={op.description}
            more_info={op.more_info}
            info_image={op.info_image}
        />);

    return(
        <div className="capabilities-page">
            <div className="title">
                Фитнес-зоны
            </div>
            <div className= "description">
                Мы внимательны к мелочам. Заботимся о вашем времени и результате. Помогаем тренироваться с удовольствием.
            </div>
            <section className="grid grid-cols-4 gap-3">
                {elementComponents}
            </section>
        </div>
    )
}